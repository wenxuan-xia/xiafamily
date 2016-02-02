function find_child(oldsystem_id, member, prefix) {
  var str = ""
  var flag = 0
  // console.log(oldsystem_id)
  // console.log(member.length)
  for (var i=0; i<member.length; i++) {
    if (member[i].belongs_to == oldsystem_id) {
      // console.log(member[i])
      if (flag == 0) {
        str += "<div class='collapse' id='"+prefix+"'>"
        flag = 1
      }
      str += "<a href='./#"+prefix+"-"+(i+1)+"' class='list-group-item gen"+member[i].generation+"', data-toggle='collapse' data-parent='#"+prefix+"'>"
      str += "<i class='fa circle-icon "
      mycolor = "yellow"
      switch (member[i].generation) {
        case "2":
          mycolor = "yellow"
          break;
        case "3":
          mycolor = "blue"
          break
        case "4":
          mycolor = "orange"
          break
        case "5":
          mycolor = "green"
          break
        default:
          break;
      }
      str += mycolor
      str += "'>"+member[i].generation+"</i>&nbsp;&nbsp;"+member[i].name
      if (member[i].gender == "男") {
        str += "<i class='fa fa-male'></i>"
      } else {
        str += "<i class='fa fa-female'></i>"
      }
      if ((member[i].married === true)&&(member[i].spouse_name!="empty")) {
        str += "<span class='info'>配&nbsp;&nbsp;" + member[i].spouse_name
        str += "</span>"
      }
      childstr = find_child(member[i].oldsystem_id, member, prefix + "-" + (i+1))
      if (childstr != "") {
        str += "<i class='fa fa-plus'></i>"
      }
      str += "</a>"
      str += childstr
    }
  }
  if (flag == 1) {
    str +="</div>"
  }
  return str
  return ""
}
function find_starter(member) {
  var str = ""
  var counter = 0
  for (i=0; i<member.length; i++) {
    if (member[i].generation == 1) {
      counter += 1
      str += "<div class='col-sm-6 col-md-4 fang'>"
      str += "<div id='MainMenu'>"
      str += "<div class='list-group panel'>"
      str += "<div class='list-group-item list-group-item-success gen1'>"
      str += "<a href='./#"+counter+"' data-toggle='collapse' data-parent='#MainMenu'><span class='fang-num'>"+member[i].house+"</span>"+member[i].name+"</a>"
      if (member[i].gender == "男") {
        str += "<i class='fa fa-male'></i>"
      } else {
        str += "<i class='fa fa-female'></i>"
      }
      // str += "<i class='fa fa-info-circle fa-6' data-toggle='modal' data-target='#1-info'"
      str += "</div>"
      str += find_child(member[i].oldsystem_id, member, ""+counter)
      str += "</div>"
      str += "</div>"
      str += "</div>"

    }
  }
  var container = $("#Gene")
  container.html(str)
}

$(document).ready(function() {

  $.ajax({
    datatype : "json",
    url : "./getWholeFamilyMembers",
    success: function(rst) {
      member = JSON.parse(rst)
      find_starter(member)

    },

  })
})
