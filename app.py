import streamlit as st
import boto3
from collections import Counter

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

# Calculate top 3 plates by number of entries
plate_counts = Counter([plate['texto_matricula'] for plate in plates])
top_3 = plate_counts.most_common(3)

st.subheader("🏆 Top 3 Plates by Entries")
for i, (plate, count) in enumerate(top_3, 1):
    st.write(f"{i}. 🪪 {plate} — {count} entries")

st.subheader("📜 All Plates")
for plate in plates:
    st.write(f"🪪 {plate['texto_matricula']} — ⏱ {plate['timestamp']}")
