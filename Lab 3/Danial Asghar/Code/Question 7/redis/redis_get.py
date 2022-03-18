import redis        # pip install redis
ip='34.130.248.159';
r = redis.Redis(host=ip, port=6379, db=0,password='SOFE4630U')
v=r.get('image1');
with open("./recieved1.jpg", "wb") as f:
    f.write(v);

v=r.get('image2');
with open("./recieved2.jpg", "wb") as f:
    f.write(v);

v=r.get('image3');
with open("./recieved3.jpg", "wb") as f:
    f.write(v);
