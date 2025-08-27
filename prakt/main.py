from stol6_2 import main
from stol6_1 import proc_main
from stol6_3 import async_main

if __name__ == '__main__':
    try:
        # thread_main()
        proc_main()
        async_main()
    except Exception as error:
        print(error.__class__.__name__)