var table = document.getElementById('tb');

var tab = document.getElementById('tab').value;

var tabb = document.getElementById('tabb').value;

var array =  [];

        for(var i=0;i<tab.length;i++){
            array.push(tab);

        }

        
        
        
        for(var i=0;i<array.length;i++){
            var name = array[i].split(',')[0];
            var age = array[i].split(',')[1];
            
            var tr = document.createElement("tr");
            tr.innerHTML="<td>"+i+"</td> <td>"+name+"</td> <td>"+age+"</td>";
            table.appendChild(tr);
        }
        
        function Search(){
            var text = document.getElementById('textbox').value;
            if(text.trim().length==0){
                Reset();
                return;
            }
            
            var TRS = table.getElementsByTagName('tr');
            var name = "";
            for(var i = 1; i<TRS.length; i++){
                name = TRS[i].getElementsByTagName('td')[1].innerHTML;
                if(name.toLowerCase().startsWith(text.trim().toLowerCase()) || name.toLowerCase().indexOf(text.trim().toLowerCase()) != -1){
                    TRS[i].style.fontSize = "14px";
                    TRS[i].style.height="40px";
                    TRS[i].style.visibility="visible";
                }
                else{
                    TRS[i].style.fontSize = "0px";
                    TRS[i].style.height="0px";
                    TRS[i].style.visibility="hidden";
                }
            }
        }
        
        function Reset(){
            var TRS = table.getElementsByTagName('tr');
            for(var i = 1; i<TRS.length; i++){
                    TRS[i].style.fontSize = "14px";
                    TRS[i].style.height="40px";
                    TRS[i].style.visibility="visible";
                }
        }
        
        Reset();

        var x = ["un", "deux", "trois" ];

