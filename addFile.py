from myClass import obj1

s3_client = obj1.s3_client


def put_object_in_s3_bucket(filename, bucket1):
    f = open(filename, "r")
    data = f.read()
    print(data)

    response3 = s3_client.put_object(
        ACL='private',
        Body=data,
        Bucket=bucket1,
        Key=filename,
    )
    return response3
