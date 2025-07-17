from tweaker.core.tweaker import Tweaker 
import re
from tweaker.tests.modules.testdata.emails import valid_emails
def main():
    
    email = "no@no.com"
    
    t = Tweaker()
    
    print(t.regex.search(t.regex.common_patterns.EMAIL, email, re.VERBOSE))


if __name__ == "__main__":
    main()