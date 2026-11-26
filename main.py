
from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class BypassTunnelMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["bypass-tunnel-reminder"] = "true"
        return response

app.add_middleware(BypassTunnelMiddleware)

@app.post("/ussd", response_class=PlainTextResponse)
async def handle_ussd(
    text: str = Form(""), 
    phoneNumber: str = Form(None), 
    sessionId: str = Form(None), 
    serviceCode: str = Form(None)
):
    user_input = text.strip()

    
    if not user_input:
        return "CON Welcome to FikaMarket!\n1. Register Account\n2. Post Produce\n3. View Price\n4. Apply for a Loan"

    
    input_parts = user_input.split("*")
    main_choice = input_parts[0]  

    
    if main_choice == "1":
        
        if len(input_parts) == 1:
            return "CON Registration Menu:\nPlease enter your full name:"
        
        
        
        elif len(input_parts) == 2:
            full_name = input_parts[1]
            
            
            
            return f"END Thank you {full_name}!\nYour account registration is complete."

    elif main_choice == "2":
        
        if len(input_parts) == 1:
            return "CON Post Produce Menu:\nEnter produce name:"
        
        
        elif len(input_parts) == 2:
            produce_name = input_parts[1]
            return f"END Success!\nYour produce '{produce_name}' has been listed on FikaMarket."

    elif main_choice == "3":
        return "CON Current Prices:\n1. Maize - KES 4000\n2. Soybeans - KES 6000\n3. Groundnuts - KES 8000"
    

    elif main_choice == "4":
        if len(input_parts) == 1:
            return "CON Loan Application:\nEnter amount required:"
        
        elif len(input_parts) == 2:
            loan_amount = input_parts[1]
            return "END Your loan application has been processed successfully. Thank you!"

    
   
    