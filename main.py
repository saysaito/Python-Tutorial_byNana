from user import User
from post import Post
user_one= User("aki@aa.com","Aki","1234","Developer")
user_one.change_job_title("Senior Developer")
user_one.get_user_info()

Post_one = Post("Hello",user_one)
Post_one.get_post_info()