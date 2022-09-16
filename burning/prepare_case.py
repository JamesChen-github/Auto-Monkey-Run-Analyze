print("start prepare_case.py")
import re
import sys
import configparser
from pathlib import Path

args = sys.argv[1:]
if len(args) != 3:
    raise ValueError('usage: python prepare_config.py {job_base_name} {build_id} {build_json_name}')
job_base_name, build_id, build_json_name = args

args_dict = {}
args_dict['JOB_BASE_NAME'] = job_base_name
args_dict['BUILD_ID'] = build_id
args_dict['BUILD_DIR'] = 'image_' + build_json_name.rsplit('.', 1)[0]

print("JOB_BASE_NAME = %s" % args_dict['JOB_BASE_NAME'])
print("BUILD_ID = %s" % args_dict['BUILD_ID'])
print("BUILD_DIR = %s" % args_dict['BUILD_DIR'])

cur_path = Path(__file__).parent
conf = configparser.ConfigParser()
conf.read(cur_path / 'ts_config_template.ini')

pattern = re.compile(r'\{\s?(?!\s)([^{}]+?)\s?\}')
emmc1_path = conf['flash']['TSV_FLASH_PAC_EMMC1']
for item in pattern.finditer(emmc1_path):
    args_name = args_dict.get(item.group(1))
    if args_name is None:
        raise NameError(f'{args_name=} not found!')
    else:
        print(f'{item.group(1)} = {args_name}, {item.group(0)=}')
        conf['flash']['TSV_FLASH_PAC_EMMC1'] = conf['flash']['TSV_FLASH_PAC_EMMC1'].replace(item.group(0), args_name)
print(f'{conf["flash"]["TSV_FLASH_PAC_EMMC1"]=}')

with open(cur_path / 'ts_config.ini', 'w', encoding='utf-8') as f:
    conf.write(f)

