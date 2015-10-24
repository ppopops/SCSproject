__author__ = 'Hong'
from flask import Flask
from MongoDB import Connect
from Salle import *
from Batiment import *
from Presentation import *
from Horaire import *
app = Flask(__name__)

db = Connect()


@app.route('/SCSproject/api/getsalle', methods=['GET'])
def get_salle():
    salle = Salle(db)
    result = salle.ReturnSalle()

    i = 0
    for s in result :
        batiment = Batiment(db)
        batimentDocument = batiment.ReturnBatimentid(s["idBatiment"])
        result[i]["idBatiment"] = batimentDocument
        i = i+ 1

    return jsonify({'salle': result})

@app.route('/SCSproject/api/setsalle', methods=['POST'])
def create_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    id = "0"   #contructor will set id
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, id )
    itemID = salle.InsertSalle()

    return jsonify(salle={"_id": itemID})
    #return jsonify(result={"status": 200})


@app.route('/SCSproject/api/getsalleid/<string:salle_id>', methods=['GET'])
def get_salle_id(salle_id):
    salle = Salle(db)
    result = salle.ReturnSalleid(salle_id)
    return jsonify({'salle': result})

@app.route('/SCSproject/api/updatesalle', methods=['POST'])
def update_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    id = salle.get ("_id")
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, id )
    salle.UpdateSalle()

    return jsonify(result={"status": 200})

@app.route('/SCSproject/api/deletesalle', methods=['POST'])
def delete_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    id = salle.get("_id")   #contructor will set id
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, id )
    salle.DeleteSalle()

    return jsonify(result={"status": 200})
##################################################################################################################

@app.route('/SCSproject/api/setbatiment', methods=['POST'])
def create_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nomBatiment","")
    adresseBatiment =  batiment.get ("adresseBatiment","")
    faculteBatiment =  batiment.get ("faculteBatiment","")
    CampusBatiment =  batiment.get ("CampusBatiment","")
    id = "0"   #contructor will set id
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment , id )
    itemId = batiment.InsertBatiment()
    #print itemId

    return jsonify(batiment={"_id": itemId})
    #return jsonify(result={"status": 200})

@app.route('/SCSproject/api/getbatiment', methods=['GET'])
def get_batiment():
    batiment = Batiment(db)
    return jsonify({'batiment': batiment.ReturnBatiment()})

@app.route('/SCSproject/api/getbatimentid/<string:batiment_id>', methods=['GET'])
def get_batiment_id(batiment_id):
    batiment = Batiment(db)
    return jsonify({'salle': batiment.ReturnBatimentid(batiment_id)})

@app.route('/SCSproject/api/updatebatiment', methods=['POST'])
def update_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nomBatiment","")
    adresseBatiment =  batiment.get ("adresseBatiment","")
    faculteBatiment =  batiment.get ("faculteBatiment","")
    CampusBatiment =  batiment.get ("CampusBatiment","")
    id = batiment.get ("_id")
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment , id )
    batiment.UpdateBatiment()

    return jsonify(result={"status": 200})

@app.route('/SCSproject/api/deletebatiment', methods=['POST'])
def delete_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nomBatiment","")
    adresseBatiment =  batiment.get ("adresseBatiment","")
    faculteBatiment =  batiment.get ("faculteBatiment","")
    CampusBatiment =  batiment.get ("CampusBatiment","")
    id = batiment.get("_id")   #contructor will set id
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment, id )
    batiment.DeleteBatiment()

    return jsonify(result={"status": 200})

#######################################################################################################
#Presentation
#######################################################################################################
@app.route('/SCSproject/api/setpresentation', methods=['POST'])
def create_presentation():
    content = request.get_json(force = True)
    print content

    presentationTemp = content.get("presentation")
    presentation= presentationTemp[0]
    titre =  presentation.get ("titre","")
    nombreParticipants =  presentation.get ("nombreParticipants","")
    equipement =  presentation.get ("equipement","")
    duree =  presentation.get ("duree","")
    presentateur =  presentation.get ("presentateur","")
    id = "0"   #contructor will set id
    presentation = Presentation( db, titre ,nombreParticipants, equipement, duree ,presentateur, id )
    itemId = presentation.InsertPresentation()
    #print itemId

    return jsonify(presentation={"_id": itemId})
    #return jsonify(result={"status": 200})

@app.route('/SCSproject/api/getpresentation', methods=['GET'])
def get_presentation():
    presentation = Presentation(db)
    return jsonify({'presentation': presentation.ReturnPresentation()})

@app.route('/SCSproject/api/getpresentationid/<string:presentation_id>', methods=['GET'])
def get_presentation_id(presentation_id):
    presentation = Presentation(db)
    return jsonify({'salle': presentation.ReturnPresentationid(presentation_id)})

@app.route('/SCSproject/api/updatepresentation', methods=['POST'])
def update_presentation():
    content = request.get_json(force = True)
    print content

    presentationTemp = content.get("presentation")
    presentation= presentationTemp[0]
    titre =  presentation.get ("titre","")
    nombreParticipants =  presentation.get ("nombreParticipants","")
    equipement =  presentation.get ("equipement","")
    duree =  presentation.get ("duree","")
    presentateur =  presentation.get ("presentateur","")
    id = presentation.get ("_id")
    presentation = Presentation( db, titre ,nombreParticipants, equipement, duree , presentateur, id )
    presentation.UpdatePresentation()

    return jsonify(result={"status": 200})

@app.route('/SCSproject/api/deletepresentation', methods=['POST'])
def delete_presentation():
    content = request.get_json(force = True)
    print content

    presentationTemp = content.get("presentation")
    presentation= presentationTemp[0]
    titre =  presentation.get ("titre","")
    nombreParticipants =  presentation.get ("nombreParticipants","")
    equipement =  presentation.get ("equipement","")
    duree =  presentation.get ("duree","")
    presentateur =  presentation.get ("presentateur","")
    id = presentation.get ("_id")
    presentation = Presentation( db, titre ,nombreParticipants, equipement, duree , presentateur, id )
    presentation.DeletePresentation()

    return jsonify(result={"status": 200})

#######################################################################################################
#Horaire
#######################################################################################################
@app.route('/SCSproject/api/sethoraire', methods=['POST'])
def create_horaire():
    content = request.get_json(force = True)
    print content

    horaireTemp = content.get("horaire")
    horaire= horaireTemp[0]
    date =  horaire.get ("date","")
    idSalle =  horaire.get ("idSalle","")
    idPresentation =  horaire.get ("idPresentation","")
    heureDebut =  horaire.get ("heureDebut","")
    id = "0"   #contructor will set id
    horaire = Horaire( db, date ,idSalle, idPresentation, heureDebut, id )
    itemId = horaire.InsertHoraire()
    #print itemId

    return jsonify(horaire={"_id": itemId})
    #return jsonify(result={"status": 200})

#@app.route('/SCSproject/api/getsalle', methods=['GET'])
#def get_salle():
#    salle = Salle(db)
#    result = salle.ReturnSalle()

#    i = 0
#    for s in result :
#        batiment = Batiment(db)
#        batimentDocument = batiment.ReturnBatimentid(s["idBatiment"])
#        result[i]["idBatiment"] = batimentDocument
#        i = i+ 1

    return jsonify({'salle': result})

@app.route('/SCSproject/api/gethoraire', methods=['GET'])
def get_horaire():
    horaire = Horaire(db)
    result = horaire.ReturnHoraire()

    i=0
    for s in result:
        salle = Salle(db)
        idSalle = salle.ReturnSalleid(s["idSalle"])
        result[i]["idSalle"] = idSalle

        presentation = Presentation(db)
        idPresentation = presentation.ReturnPresentationid(s["idPresentation"])
        result[i]["idPresentation"] = idPresentation

        i = i +1
    return jsonify ({'horaire' : result})
    #return jsonify({'horaire': horaire.ReturnHoraire()})

@app.route('/SCSproject/api/gethoraireid/<string:horaire_id>', methods=['GET'])
def get_horaire_id(horaire_id):
    horaire = Horaire(db)
    return jsonify({'horaire': horaire.ReturnHoraireid(horaire_id)})

@app.route('/SCSproject/api/updatehoraire', methods=['POST'])
def update_horaire():
    content = request.get_json(force = True)
    print content

    horaireTemp = content.get("horaire")
    horaire= horaireTemp[0]
    date =  horaire.get ("date","")
    idSalle =  horaire.get ("idSalle","")
    idPresentation =  horaire.get ("idPresentation","")
    heureDebut =  horaire.get ("heureDebut","")
    id = horaire.get ("_id")
    horaire = Horaire( db, date ,idSalle, idPresentation, heureDebut, id )
    horaire.UpdateHoraire()

    return jsonify(result={"status": 200})

@app.route('/SCSproject/api/deletehoraire', methods=['POST'])
def delete_horaire():
    content = request.get_json(force = True)
    print content

    horaireTemp = content.get("horaire")
    horaire= horaireTemp[0]
    date =  horaire.get ("date","")
    idSalle =  horaire.get ("idSalle","")
    idPresentation =  horaire.get ("idPresentation","")
    heureDebut =  horaire.get ("heureDebut","")
    id = horaire.get ("_id")
    horaire = Horaire( db, date ,idSalle, idPresentation, heureDebut, id )
    horaire.DeleteHoraire()

    return jsonify(result={"status": 200})

if __name__ == '__main__':
    app.run(host='0.0.0.0')