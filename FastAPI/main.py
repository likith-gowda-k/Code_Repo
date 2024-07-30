from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    data=  {
                "message": "Hello World",
                "message1": "Hello World",
                "message2": "Hello World",
                "message3": "Hello World",
                
            }
    return data


@app.get("/user/{user_id}/")
async def user_data(user_id):
    return {user_id: f"This is the data for {user_id}"}