import streamlit as st
import boto3

dynamodb = boto3.resource('dynamodb',region_name='eu-north-1')
table = dynamodb.Table('matriculas')

st.title("🔍 License Plate Tracker")

response = table.scan()
plates = sorted(response["Items"], key=lambda x: x["timestamp"], reverse=True)

for plate in plates:
    st.write(f"🪪 {plate['plate']} — ⏱ {plate['timestamp']}")
