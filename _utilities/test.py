__author__ = 'yi-linghwong'

lines = open('../fb_data/posts/raw_fb_posts_20160226.csv','r').readlines()
#lines = open('test.csv','r').readlines()

print (len(lines))

posts = []

for line in lines:
    spline = line.replace('\n','').split(',')

    spline[8] = spline[8].replace('\t',' ')

    posts.append(spline)

f = open('../fb_data/posts/raw_fb_posts_20160226_1.csv','w')

for p in posts:
    f.write(','.join(p)+'\n')

f.close()




