import azure.functions as func
import logging

app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def send_email_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Start function")
    logging.info("folder func_user_disable version 1.0.0")
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.", status_code=200
    )
