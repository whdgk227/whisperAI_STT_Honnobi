from datetime import timedelta
import os

def convertSegmentToSrt(result, saveFileName):
    print(saveFileName + " - 자막 생성을 시작합니다.")
    saveFilePath = "./"
    deleteExistOutputFile(saveFilePath, saveFileName)
    print("자막 생성이 완료되었습니다.\n" + saveFileName + " 파일명으로 저장을 시작합니다.")
    for segment in result:
        startTime =str(timedelta(seconds=segment['start']))
        endTime = str(timedelta(seconds=segment['end']))
        if ("." not in startTime):
          startTime = startTime + '.000000'
        if ("." not in endTime):
          endTime = endTime + '.000000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
        srtFilename = os.path.join(saveFilePath, saveFileName)
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)
    files.download(saveFileName)
    print("파일 다운로드가 완료 되었습니다. 저장 된 " + saveFileName + " 파일을 다운로드 받아 주세요!")

    return srtFilename

def deleteExistOutputFile(saveFilePath, saveFileName):
    if os.path.exists(saveFilePath + saveFileName):
        os.remove(saveFilePath + saveFileName)