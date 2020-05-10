# put outputs here
output "url" {
  value= join("",["http://",docker_container.nginx-server.ports[0].ip,":",docker_container.nginx-server.ports[0].external])
}
