from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import urlopen


def url_search():
    search_url = input("Enter a website URL: ").strip()

    if not search_url:
        print("Error: Please enter a URL.")
        return

    if "://" not in search_url:
        search_url = "https://" + search_url

    try:
        parsed = urlsplit(search_url)
        if parsed.scheme.lower() not in ("http", "https") or not parsed.hostname:
            print("Error: Please enter an http or https web address.")
            return

        with urlopen(search_url, timeout=10) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            content = response.read().decode(charset, errors="replace")
            print("Connected URL:", response.url)
            print("Response Content:")
            print(content[:200])  # Print the first 500 characters of the response content

    except HTTPError as error:
        print(f"HTTP Error: {error.code} {error.reason}")
    except URLError as error:
        print(f"Connection Failed: {error.reason}")
    except TimeoutError:
        print("Error: Connection or response timeout exceeded.")
    except (ValueError, UnicodeError) as error:
        print(f"URL Format Error: {error}")
    except LookupError as error:
        print(f"Response Encoding Error: {error}")


if __name__ == "__main__":
    url_search()
