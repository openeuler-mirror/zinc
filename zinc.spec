Name:           zinc
Version:        0.3.1
Release:        7
Summary:        A stand-alone version of incremental scala compiler
License:        ASL 2.0
URL:            https://github.com/typesafehub/zinc
BuildArch:      noarch

Source0:        https://github.com/typesafehub/zinc/archive/v%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/com/typesafe/zinc/zinc/%{version}/zinc-%{version}.pom
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Fix file filtering
Patch0001:      0001-Fix-file-filtering.patch

BuildRequires:  javapackages-local mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-sbt:incremental-compiler) mvn(com.martiansoftware:nailgun-server)

%description
Zinc is a stand-alone version of sbt's incremental compiler.

%prep
%autosetup -n zinc-%{version} -p1
rm -rf src/scriptit dist nailgun project

cp %{SOURCE1} pom.xml
cp %{SOURCE2} LICENSE.txt

%pom_xpath_remove "pom:dependency[pom:classifier='sources']"
%pom_change_dep :incremental-compiler org.scala-sbt:

%build
scalac -cp $(build-classpath sbt nailgun) src/main/scala/com/typesafe/zinc/*
jar cf zinc.jar com
%mvn_artifact pom.xml zinc.jar

%install
%mvn_install

%files -f .mfiles
%doc README.md LICENSE.txt

%changelog
* Wed Mar 4 2020 wangzhishun <wangzhishun1@huawei.com> - 0.3.1-7
- Package init
