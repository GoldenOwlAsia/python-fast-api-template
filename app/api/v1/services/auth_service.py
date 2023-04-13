from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Hàm kiểm tra thông tin đăng nhập
def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except:
        return False

# Hàm mã hóa mật khẩu
def get_password_hash(password):
    return pwd_context.hash(password)

# Hàm tạo token JWT
def create_jwt_token(user_id: str):
    payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(minutes=30)}
    token = jwt.encode(payload, "secret_key")
    return token

# Hàm xác thực token JWT
def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        user_id = payload["user_id"]
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
