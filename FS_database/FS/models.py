from django.db import models

# Create your models here.

class GPO(models.Model) : # 간납처
    GPO_code = models.IntegerField(primary_key=True) # 간납처 코드
    GPO_name = models.CharField()                    # 간납처 명
    manager = models.CharField()                     # 담당자
    condition = models.CharField()                   # 조건
    month = models.IntegerField()                    # 개월
    agreement = models.CharField()                   # 약정
    transaction = models.CharField()                 # 거래
    purchasing_manager = models.CharField()          # 구매담당자
    purchasing_manager_phone = models.CharField()    # 구매담당자 핸드폰
    purchasing_manager_email = models.EmailField()   # 구매담당자 이메일
    cashier_phone = models.CharField()               # 계산담당자 핸드폰
    cashier_email = models.EmailField()              # 계산담당자 이메일

class Product(models.Model) : # 제품
    product_code = models.CharField(primary_key=True)
    product_name = models.CharField()
    packaging_unit = models.CharField()
    pharmacist = models.CharField()
    insurance_code = models.CharField()
    standard_code = models.CharField()
    base_price = models.IntegerField()
    salary = models.IntegerField()
    division = models.CharField()
    ingredient_code = models.CharField()

class Purchasers(models.Model) : # 매입 거래처
    Puchaser_code = models.CharField(primary_key=True)
    Puchaser_name = models.CharField()
    address = models.CharField()
    phone_number = models.CharField()
    company_registration_number = models.CharField()
    representative = models.CharField()
    email = models.EmailField()  
    credit_information = models.CharField()
    terms_of_payment = models.CharField()
    note = models.CharField()

class Sales_Account(models.Model) : # 매출 거래처
    Sales_code = models.CharField()
    Sales_name = models.CharField()
    address = models.CharField()
    phone_number = models.CharField()
    company_registration_number = models.CharField()
    representative = models.CharField()
    email = models.EmailField()  
    credit_information = models.CharField()
    recovery_condition = models.CharField()
    note = models.CharField()

class COA(models.Model) : # 계정
    coa_code = models.IntegerField(primary_key=True)
    coa_name = models.CharField()
    account_category =  models.CharField()
    account_subcategory = models.CharField()
    account_subcategory = models.CharField()
    financial_statements = models.CharField()
    note = models.TextField()

class Raw_Materials(models.Model) : # 원부재료 리스트
    raw_materials_code = models.IntegerField(primary_key=True)
    raw_materials_name = models.CharField()
    packaging_unit = models.CharField()
    purchaser = models.CharField()
    standard_unit_price = models.IntegerField()
    note = models.CharField()
    
class Goods(models.Model) : # 상품 리스트
    goods_code = models.IntegerField(primary_key=True)
    goods_name = models.CharField()
    packaging_unit = models.CharField()
    purchaser = models.CharField()
    standard_unit_price = models.IntegerField()
    note = models.CharField()


