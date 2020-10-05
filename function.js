var conocimiento = {
	"CON":[
		{"TieneCon": [["tortuga","garras"],
					 ["tortuga","proteccion queratina"],
					 ["Gallo","proteccion queratina"],
					 ["Gallo","garras"],
					 ["Cocodrilo","proteccion queratina"],
					 ["Cocodrilo","garras"],
					 ["Iguana","proteccion queratina"],
					 ["Iguana","garras"],
					 ["Gato","G. mamarias"],
					 ["Gato","pelo"],
					 ["Gato","garras"],
					 ["Ballena","G. mamarias"],
					 ["Oso","G. mamarias"],
					 ["Oso","pelo"],
					 ["Oso","garras"],
					 ["Delfin","G. mamarias"]]},

		{"ViveCon": [["tortuga","Tierra"],
					["tortuga","Agua"],
					["Gallo","Tierra"],
					["Cocodrilo","Tierra"],
					["Cocodrilo","Agua"],
					["Iguana","Tierra"],
					["Gato","Tierra"],
					["Ballena","Agua"],
					["Oso","Tierra"],
					["Delfin","Agua"]]},
		{"ConEs": [["proteccion queratina","Oviparo"],
				  ["Oviparo","Sauropsidos"],
				  ["Sauropsidos","tetrapodos"],
				  ["G. mamarias","viviparo"],
				  ["viviparo","Mammalia"],
				  ["Mammalia","tetrapodos"],
				  ["tortuga","Oviparo"],
				  ["Gallo","Oviparo"],
				  ["Cocodrilo","Oviparo"],
				  ["Iguana","Oviparo"],
				  ["Gato","viviparo"],
				  ["Oso","viviparo"],
				  ["Ballena","viviparo"],
				  ["Delfin","viviparo"],
				  ["tetrapodos","vertebrado"]]}
		]
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

function inicio(){
		var animal= prompt("Ingrese un animal");
		var Tiene = prompt(animal+" tiene");
		var vive = prompt(animal+" ¿vive en?");
		var es = prompt(animal+" es");
		var res = "";

		var TieneCon = conocimiento["CON"][0]["TieneCon"];
		var ViveCon = conocimiento["CON"][1]["ViveCon"];
		var ConEs = conocimiento["CON"][2]["ConEs"];

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