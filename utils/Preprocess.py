import pandas as pd

def Reader(file_path, file_list):
    """
    경로 내 파일목록을 받아, 파일명과 파일내용을 데이터프레임으로 반환하는 함수입니다.
    입력 : 파일 경로, 파일 목록
    출력 : 데이터프레임(파일명 및 Text)
    """
    data = []
    for i in range(len(file_list)):
        file = open(file_path+"\\"+file_list[i], "r", encoding="utf-8")
        text = file.read()
        data.append((file_list[i],text))
        file.close()
    df = pd.DataFrame(data, columns=['file_name','text'])
    return df

def Preprocessor(data):
    """
    텍스트를 전처리하는 함수입니다
    """
    data['text'] = data['text'].replace('\n', ' ')
    return data