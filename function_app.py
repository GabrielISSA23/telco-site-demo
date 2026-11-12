import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    tenure = req.params.get("tenure")
    monthly = req.params.get("monthly")
    techsupport = req.params.get("techsupport")

    if tenure and monthly and techsupport:
        prediction = make_prediction(
            tenure=float(tenure),
            MonthlyCharges=float(monthly),
            TechSupport_yes=float(techsupport),
        )
        return func.HttpResponse(
            f"Hello, prediction is {prediction}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass the 3 independant variables (tenure,monthly,techsupport) in the query string or in the request body for a personalized response.",
            status_code=200,
        )
