import streamlit as st
import boto3

aws_access_key = st.secrets["aws"]["aws_access_key_id"]
aws_secret_key = st.secrets["aws"]["aws_secret_access_key"]

dynamodb = boto3.resource(
    'dynamodb',
    region_name='eu-north-1',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# dynamodb = boto3.resource('dynamodb',region_name='eu-north-1')
table = dynamodb.Table('matriculas')

st.title("🔍 License Plate Tracker")

response = table.scan()
plates = sorted(response["Items"], key=lambda x: x["timestamp"], reverse=True)

for plate in plates:
    st.write(f"🪪 {plate['texto_matricula']} — ⏱ {plate['timestamp']}")
