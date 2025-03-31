### Running the app

1. create a virtual environment 
```
py -3 -m venv venv
venv\Scripts\activate
```
2. install dependencies
```
pip install -r requirements.txt
```
3. ensure you have a .env file with OPENAI_API_KEY in the root of the project.
4. Run the app 
```
python app.py
```
5. Test the app
```
curl -X GET http://localhost:5000/summarize  -H "Content-Type: application/json"  -d "{\"text\": \"The Industrial Revolution, which took place from the 18th to 19th centuries, was a period during which predominantly agrarian, rural societies in Europe and America became industrial and urban. It marked a major turning point in history; almost every aspect of daily life was influenced in some way. Particularly, it saw significant advancements in machinery, transportation, and manufacturing. As a result, it laid the foundation for the modern economic world.\"}" 
```