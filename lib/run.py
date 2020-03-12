import json
def a():
    with open('data/test_data.json', 'r')as f:
        item = json.load(f)
    print("This is a {}".format(item['test_input']))

if __name__=='__main__':
    a()

