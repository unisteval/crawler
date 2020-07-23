# 유니스트 개설강좌목록 

`get_file`함수를 통하여 개설강좌목록을 엑셀로 불러올 수 있습니다.

``` python
get_file(year, semester, string, file_name)
```

1. `year` 검색할 연도를 `int`형태로 넣습니다.
2. `semester` 검색할 학기를 다음 `string`중 하나의 형태로 넣습니다. `1st`,`summer`,`2nd`,`3rd`,`winter` 아니면, 각 학기를 의미하는 숫자인 `90`,`91`,`92`,`93`을 `int`형태로 넣는것도 가능합니다.
3. `string` 검색할 문자열을 `string`형태로 넣습니다.
4. `file_name` 저장하고자 하는 파일위치와 이름을 넣습니다,

사용 예시는 `test.py`에 있습니다.
