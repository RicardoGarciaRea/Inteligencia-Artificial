	//Variable donde se guada nuestro json
	let datos;
	//Funcion para traer datos
	function traerDatos(){
		const xhttp = new XMLHttpRequest();
		xhttp.open('GET','datos.json',true);
		xhttp.send();
		  xhttp.onreadystatechange = function(){  	
			if(this.readyState == 4 && this.status ==200){
				datos = JSON.parse(this.responseText);
			}
		  }
	}
	traerDatos();

	function cerrar(){
		window.close();
	}

    function countPal(A,CON,NA){
      	let N = [];
       	for(var i = 0; i < CON.length; i++){
       		if(CON[i][0] == A){
       			N.push(CON[i][1]);
       			console.log("a",CON[i][1])
       		}
       	}
        	return N;
        }

        function EncontrarTiene(A,NA){
        	let pos = NA.indexOf(A);
        	if(pos == -1){
        		return false;
        	}
        	else{
        		return true;
        	}
        }

		function esta(P,L,CON){
			var LdP = buscar(P,CON);
			var v;
			if(LdP == L){
				return true;
			}
			else if(LdP == false){
				return false;
			}
			else{
				return (esta(LdP,L,CON));
			}
		}

		function buscar(P,CON){
			var i = 0;
			var l = CON.length;
			while(i < l){
				if(P == CON[i][0]){
					//recorreMatriz(CON[i][1],CON);
					console.log(CON[i][1]);
					return CON[i][1];
				}
				i++;
			}
			return false;
		}

		//inicio de todo
	function inicio(a,t,v,e){
			var animal= a;
			var Tiene = t;
			var vive = v;
			var es = e;
			var res = "";

			var TieneCon = datos["CON"][0]["TieneCon"];
			var ViveCon = datos["CON"][1]["ViveCon"];
			var ConEs = datos["CON"][2]["ConEs"];

			let NA = [];
			NA = countPal(animal,TieneCon,NA);
			let pos = EncontrarTiene(Tiene,NA);

			let VA = [];
			VA = countPal(animal,ViveCon,VA);
			let posVive = EncontrarTiene(vive,VA);

			var x = esta(animal,es,ConEs);
			
			if(pos){
				res = "El/La "+animal+" tiene "+Tiene;
			}
			else{
				res ="El "+animal+" no tiene "+Tiene;
			}
			if(posVive){
				res = res+" y vive en "+vive;
			}else{
				res = res+ " y no vive en "+vive;
			}
			if(x){
				res = res+ " es "+es;
			}else{
				res = res+ " no es "+es;
			}

			document.getElementById("resultado").innerHTML = res; 
	}