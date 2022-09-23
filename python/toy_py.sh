# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Last Modified by: Hengyu Shang(shanghengyu997@outlook.com)
# @Last Modified time: 2022-09-05
# @Version: v0.1

TOY_PY_DIR=$(dirname $(readlink -f "$0"))
source ${TOY_PY_DIR}/toy_py_env.sh
TOY_PY_RUNTIME="PYTHONPATH=${TOY_PY_DIR}/lib ${TOY_PY_INTERPRETER}"
alias toy_py_runtime=${TOY_PY_RUNTIME}

for py_script in $(ls ${TOY_PY_DIR}/script); do
    alias ${py_script%.*}="${TOY_PY_RUNTIME} ${TOY_PY_DIR}/script/${py_script}"
done

alias chk_torrent="${TOY_PY_RUNTIME} -m torrentfile recheck"
alias beet="PATH=${TOY_PY_ENV_DIR}:$PATH beet"
