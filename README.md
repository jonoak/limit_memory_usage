# limit_memory_usage.py
<br/>
<h2> Use this module to limit the amount of memory your python function is using. </h2>

<h5>
<br/><br/><br/>
<b><i><h3>Install with pip:</h3></i></b> <br/> 
pip install git+https://github.com/jonoak/limit_memory_usage.git

<br/><br/>
<b><i><h3>Use as decorator:</h3></i></b><br/>
import limit_memory_usage as lmu <br/>

@lmu.memory(percentage=0.8) <br/>
def main():<br/>
&nbsp;&nbsp;print("using only 80% of memory")

  </h5>

