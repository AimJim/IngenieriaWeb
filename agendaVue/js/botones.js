var app4 = new Vue({
	el:'#app-4',
	data:{
        users:[],
        nombreI:'',
        emailI:'',
        telefonoI:''
    },
    methods:{
        anadirUser: function(event){
            event.preventDefault();
            this.users.push({nombre:this.nombreI, email:this.emailI, telefono:this.telefonoI});
            this.nombreI='';
            this.emailI='';
            this.telefonoI='';
        },
        borrar: function(nombre, email){
            for (var i = 0; i < this.users.length; i++) {
                if(this.users[i].nombre == nombre && this.users[i].email == email){
                    this.users.splice(i,1);
                    break;
                }
            }
        }
    },
	})