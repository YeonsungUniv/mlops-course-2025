import boto3
import os

# S3 클라이언트 생성
s3 = boto3.client('s3')
bucket_name = os.environ.get('BUCKET_NAME')

try:
    # 버킷 내 파일 목록 조회
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix='week1/')
    print("S3 파일 목록:")
    for obj in response.get('Contents', []):
        print(f"  {obj['Key']}")
    
    print("S3 연결 테스트 성공!")
except Exception as e:
    print(f"오류: {e}")
