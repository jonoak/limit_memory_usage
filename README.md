# limit_memory_usage.py
<br/><br/><br/>
<b><u>Install with pip:</u></b> <br/> <br/>
pip install git+https://github.com/jonoak/limit_memory_usage.git

<br/><br/>
<b><u>Use as decorator:</u></b>
<br/><br/>
<code>
import limit_memory_usage as lmu <br/>

@lmu.memory(percentage=0.8) <br/>
def main():<br/>
&nbsp;&nbsp;print("using only 80% of memory")
</code>