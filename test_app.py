from app import app

def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"AI Healthcare Solutions Delivery System" in response.data

def test_generate_solution():
    response = app.test_client().post(
        "/",
        data={"requirement": "Medicine production and batch tracking"},
    )
    assert response.status_code == 200
    assert b"Production Management" in response.data
    assert b"Batch Tracking" in response.data

def test_empty_requirement():
    response = app.test_client().post("/", data={"requirement": ""})
    assert response.status_code == 200
    assert b"Please enter your requirements." in response.data
