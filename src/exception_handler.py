
import sys
f
def error_message_details(error , error_details : sys):
    _ , _ , tb_exc = error_details.exc_info()
    filename = tb_exc.tb_frame.f_code.co_filename
    lineno = tb_exc.tb_lineno
    error_message = f'\n Error Occured in the python script {filename} \n At Line No : {lineno} \n Error : {str(error)}'
    return error_message



class CustomException(Exception):
    def __init__(self, error_message , error_details):
        super().__init__(error_message)
        self.error_details = error_message_details(error_message,error_details)

    def __str__(self):
        return self.error_details
    


if __name__ == "__main__":
    try : 
        a = 1 
        b = 0
        print(a/b)
    except Exception as e :
        raise CustomException(e,sys)