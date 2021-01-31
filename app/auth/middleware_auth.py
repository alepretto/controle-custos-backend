import jwt
import time
from fastapi import Request
from fastapi.responses import JSONResponse

from config.environment import JWT_ALGORITHM, JWT_SECRET


async def auth_user(request: Request, call_next):
    if str(request.url).split("/")[-1] != "login":
        try:
            jwt_token = request.headers["authorization"].split(" ")[1]
            payload = jwt.decode(jwt_token, JWT_SECRET, algorithms=JWT_ALGORITHM)

            time_expires = payload.get("expires")
        except:
            return JSONResponse({"error": "Token missing"}, status_code=401)

        if time.time() > time_expires:
            return JSONResponse({"error": "Token expire"}, status_code=401)

    response = await call_next(request)
    return response
