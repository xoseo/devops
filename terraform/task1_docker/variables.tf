# put variables here
variable nginx_version {
  description = "Nginx version"
  default     = "nginx:stable"
}
variable phpfpm_version {
  description = "PHP-FPM version"
  default     = "php:7.4.5-fpm"
}
variable network_name {
  description = "Network name"
  default     = "epam"
}
