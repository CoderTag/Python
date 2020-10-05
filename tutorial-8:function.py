def hello_func(greeting, name='You'):
    print('{} {}'.format(greeting,name))

hello_func("Welcome")
hello_func("Welcome",name="Kas")  # named argument should always come at the end

def student_info(*args,**kwargs):
    """ This is called doc string. Expain what function is doing.
    It is good practice to have a doc string for each funciton """
    print(args)         # it is tuple
    print(kwargs)       # it is dictionary

student_info("Science","Math",name="kas",age=40)

courses = ['Science', 'Math']
info = {'name': 'kas', 'age': 40}
student_info(courses,info)      # it will not separate courses and info in function definition.
student_info(*courses,**info)   # * will unpack list and ** will unpack dictionary before passing to function
