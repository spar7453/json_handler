from json_handler.test import Test, t

if __name__ == '__main__':
    j = t.to_json()
    print(j)
    # load = json_tricks.loads(json, cls_lookup_map={"__instance_type__": ["pyson.pyson", "Test"]})
    load = Test.from_json(j)
    print(load)
