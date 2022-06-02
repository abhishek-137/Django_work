from datetime import date
from django.http import Http404
from django.shortcuts import render

about={
    "Auth_name":"Abhishek's Blog",

    "Introduction":"Hi, I am Abhishek and I love to blog about tech and the world!",
   
    "Description": """
    I love programming, I love to help others and I enjoy exploring new
    technologies in general!

        My goal is to keep on growing as a developer - and if I could help you do
    the same, I'd be very happy!
    """
}

posts =[
    {
"slug": "the-beauty-of-nature",
 "image": "forests.jpg",

"author": "Abhishek",
 "date": date(2021, 7, 21),

"title": "A trip to forest",

"excerpt": "There's nothing like the calmness you get when walking in the forests! And I felt great while I was walking and exploring the views,calmness and greenery!",

"content": """
    Delectus dignissimos quis hic nobis architecto, hic molestiae voluptate minima in optio obcaecati expedita rerum?
    Repellat recusandae fugit alias doloribus labore, inventore nulla expedita architecto libero eum, deleniti doloribus 
    qui culpa architecto incidunt ab, adipisci laudantium quasi ab nam quidem, accusamus nisi eligendi voluptatem.
    Deleniti repellat labore dolores recusandae provident similique? Eum laudantium nisi dolore aperiam a veniam,
    modi libero error ducimus laborum inventore id, quisquam reprehenderit harum accusamus corrupti magni inventore expedita maxime?

    Blanditiis velit labore assumenda commodi dolorem laboriosam, impedit voluptate ipsam modi 
    excepturi, reiciendis debitis asperiores amet ipsa facere ex dicta, officiis dolorem 
    laboriosam quis at? Voluptas porro ad voluptatum doloremque nesciunt praesentium 
    fugiat atque dignissimos natus mollitia? Dolor sint ut praesentium tenetur quia autem ducimus,
    voluptas cum quos iure rerum sint optio consequatur cumque, ipsa eum modi quisquam cupiditate excepturi?
    Voluptas assumenda repudiandae esse delectus doloremque praesentium enim harum, saepe aspernatur 
    odio iusto soluta, accusamus quam ducimus minus harum eius itaque, repellat incidunt sit.
     
"""},
    
    {

"slug": "hike-in-the-mountains",
 "image": "mountains.jpg",

"author": "Abhishek",
 "date": date(2021, 8, 21),

"title": "Mountain Hiking",

"excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",

"content": """
    Delectus dignissimos quis hic nobis architecto, hic molestiae voluptate minima in optio obcaecati expedita rerum?
    Repellat recusandae fugit alias doloribus labore, inventore nulla expedita architecto libero eum, deleniti doloribus 
    qui culpa architecto incidunt ab, adipisci laudantium quasi ab nam quidem, accusamus nisi eligendi voluptatem.
    Deleniti repellat labore dolores recusandae provident similique? Eum laudantium nisi dolore aperiam a veniam,
    modi libero error ducimus laborum inventore id, quisquam reprehenderit harum accusamus corrupti magni inventore expedita maxime?

    Blanditiis velit labore assumenda commodi dolorem laboriosam, impedit voluptate ipsam modi 
    excepturi, reiciendis debitis asperiores amet ipsa facere ex dicta, officiis dolorem 
    laboriosam quis at? Voluptas porro ad voluptatum doloremque nesciunt praesentium 
    fugiat atque dignissimos natus mollitia? Dolor sint ut praesentium tenetur quia autem ducimus,
    voluptas cum quos iure rerum sint optio consequatur cumque, ipsa eum modi quisquam cupiditate excepturi?
    Voluptas assumenda repudiandae esse delectus doloremque praesentium enim harum, saepe aspernatur 
    odio iusto soluta, accusamus quam ducimus minus harum eius itaque, repellat incidunt sit. 
"""
},

    {
"slug": "Sunday-beach-day",
"image": "beach.jfif",

"author": "Abhishek",
"date": date(2021, 9, 21),

"title": "Sunday-Beach Day",

"excerpt": "There's nothing like the experience of waves hitting you on beaches! Surfing on these waves can also be a fun activity to do",

"content": """
    Delectus dignissimos quis hic nobis architecto, hic molestiae voluptate minima in optio obcaecati expedita rerum?
    Repellat recusandae fugit alias doloribus labore, inventore nulla expedita architecto libero eum, deleniti doloribus 
    qui culpa architecto incidunt ab, adipisci laudantium quasi ab nam quidem, accusamus nisi eligendi voluptatem.
    Deleniti repellat labore dolores recusandae provident similique? Eum laudantium nisi dolore aperiam a veniam,
    modi libero error ducimus laborum inventore id, quisquam reprehenderit harum accusamus corrupti magni inventore expedita maxime?

    Blanditiis velit labore assumenda commodi dolorem laboriosam, impedit voluptate ipsam modi 
    excepturi, reiciendis debitis asperiores amet ipsa facere ex dicta, officiis dolorem 
    laboriosam quis at? Voluptas porro ad voluptatum doloremque nesciunt praesentium 
    fugiat atque dignissimos natus mollitia? Dolor sint ut praesentium tenetur quia autem ducimus,
    voluptas cum quos iure rerum sint optio consequatur cumque, ipsa eum modi quisquam cupiditate excepturi?
    Voluptas assumenda repudiandae esse delectus doloremque praesentium enim harum, saepe aspernatur 
    odio iusto soluta, accusamus quam ducimus minus harum eius itaque, repellat incidunt sit. 
"""
}
]

def get_date(post):
    return post["date"]

def starting_page(request):
    latest_posts=sorted(posts,key=get_date)
    latest_posts=latest_posts[-3:]
    return render(request, "blog/index.html",{"posts":latest_posts,"about":about})

def all_posts(request):
    return render(request, "blog/all_posts.html",{"posts":posts})

def post_detail(request, slug): 
    identified_post = next(post for post in posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
    