# Python 코드 도우미

Python 3.10 이상에서 사용하는 한국어 터미널 도우미입니다.
선택한 Python 파일의 동작과 오류를 설명하고 후속 질문에 답합니다.
분석 대상 파일을 변경하거나 실행하지 않습니다.

## 실행 (PowerShell)

```powershell
python -m pip install -r requirements-code-helper.txt
$env:OPENAI_API_KEY = "본인의 API 키"
python code_helper.py url_test01.py
```

API 키는 소스 파일에 작성하지 마세요. 실행한 터미널의 환경변수로 설정합니다.
AI 분석에는 선택한 파일 전체와 질문, 최근 대화가 OpenAI API로 전송되며
API 이용 요금이 발생할 수 있습니다. 전송할 파일에 비밀정보가 없는지 확인하세요.
이 도우미는 서버에 응답을 저장하지 않도록 `store=False`를 사용하며,
로컬 대화는 프로그램 종료 시 사라집니다. 이는 서비스 전체의 데이터 보존 정책을
변경하는 설정은 아닙니다.

기본 모델은 `gpt-6-astra`이며, 계정에서 사용할 수 있는 모델로 바꿀 수 있습니다.

```powershell
$env:OPENAI_MODEL = "사용할 모델 ID"
python code_helper.py url_test01.py --question "print(response)는 무엇을 출력해?"
```

`--model "모델 ID"`로도 지정할 수 있습니다. `/exit`를 입력하면 종료합니다.
대화 중에는 최초에 읽은 코드가 유지되므로 파일을 수정했다면 다시 실행하세요.
최근 6개 문답과 원본 코드를 다음 요청에 포함합니다.

## API 키 없이 문법 검사

```powershell
python code_helper.py url_test01.py --check
```

이 모드는 추가 패키지나 인터넷 연결이 필요하지 않습니다.
문법 오류가 있으면 줄 번호를 출력하고 종료 코드 1을 반환합니다.
문법 통과가 실행 성공을 보장하지 않으며 AI 설명에도 오류가 있을 수 있습니다.
Python 소스의 인코딩 선언을 지원하며 파일 크기는 100,000바이트로 제한합니다.

API 구현은 [OpenAI 공식 Responses API 문서](https://developers.openai.com/api/reference/python/resources/responses/methods/create)를 따릅니다.
