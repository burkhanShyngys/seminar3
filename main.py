#from linked_list import MyList, ListNode
from linked_class import MySet
from myclass import Calculator

st = MySet();
st2 = MySet();

st.add(Calculator(4, '+', 6))
st.add(Calculator(4, '*', 3))
st.add(Calculator(4, '/', 3))


st.remove(Calculator(4, '+', 6))
st.add(Calculator(10, '-', 6))


st2.add(Calculator(4, '*', 3))
print(st2.issubsetof(st))

st2.add(Calculator(4, '+', 6))
print(st2.issubsetof(st))


st2.remove(Calculator(4, '+', 6))
st2.add(Calculator(4, '*', 3))
st2.add(Calculator(4, '/', 3))
st2.add(Calculator(10, '-', 6))
print(st.equals(st2))

st.union(st2)
for i in st:
	i.print_ans()

