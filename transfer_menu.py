import sqlite3
import django
django.setup()
from treenav.models import MenuItem
lite_conn = sqlite3.connect("../zhihu_topic/db.sqlite3")
cur = lite_conn.cursor()
menuitems = {}

def rec_select(parent_id=2):
    sql = "select * from topics_topic where parent_id={0}"
    cur.execute(sql.format(parent_id))
    results = cur.fetchall()
    for result in results:
        topic_id = save_by_results(result)
        rec_select(topic_id)

def save_by_results(result):
    name = result[0]
    topic_id = result[2]
    follower_num = result[1]
    parent_id = result[5]
    try:
        menu_item_finded = MenuItem.objects.get(pk=topic_id)
    except:
        menu_item_finded = False
    if menu_item_finded:
        if not topic_id in menuitems:
            menuitems[topic_id] = menu_item_finded
        return topic_id
    menu_item = MenuItem(pk=topic_id)
    menu_item.label = name
    menu_item.followers = follower_num
    parent_local_finded = menuitems.get(parent_id)
    if parent_local_finded:
        menu_item.parent = parent_local_finded
    else:
        parent = MenuItem.objects.get(pk=parent_id)
        menu_item.parent = parent
        menuitems[parent_id] = parent

    menu_item.slug = name
    menu_item.save()
    menuitems[topic_id] = menu_item
    return topic_id

rec_select()
