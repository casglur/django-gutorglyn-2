from django.utils import feedgenerator

feed = feedgenerator.Rss201rev2Feed(title=u"", 
                                    link=u"", 
                                    description=u"",
                                    language=u"",
                                    )

feed.add_item(
              title="Hello",
              link=u"http://www.holovaty.com/test/",
              description="Testing."
              )

fp = open('test.rss', 'w')
feed.write(fp, 'utf-8')
fp.close()