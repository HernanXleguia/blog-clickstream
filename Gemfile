source "https://rubygems.org"

# Usa la versión estable de Jekyll
gem "jekyll", "~> 4.4.1"

# --- 🔹 Tema del sitio ---
# Elimina o comenta la línea del tema Minima (no se usa con Cayman)
# gem "minima", "~> 2.5"

# Tema Cayman
gem "jekyll-theme-cayman", "~> 0.2.0"

# --- 🔹 Plugins de Jekyll ---
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# --- 🔹 Compatibilidad con Windows ---
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# --- 🔹 Dependencias necesarias para Ruby 3.4+ ---
gem "csv"
gem "logger"
