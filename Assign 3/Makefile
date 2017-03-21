
JFLAGS = -g
JCLASS = -cp $(CLASSPATH):.:./src/:/usr/share/java/junit4.jar$(CLASSPATH):.:/opt/local/share/java/junit.jar:/opt/local/share/java/hamcrest-core.jar
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
	src/Constants.java \
	src/Destinations.java \
	src/FullSequenceException.java \
	src/GenericList.java \
	src/InvalidPointException.java \
	src/InvalidPositionException.java \
	src/InvalidRegionException.java \
	src/Map.java \
	src/Obstacles.java \
	src/PathCalculation.java \
	src/PathT.java \
	src/PointT.java \
	src/RegionT.java \
	src/SafeZone.java \
	src/TestPathCalculation.java \

MAIN = TestPathCalculation

default: classes

classes: $(JC) $(JFLAGS) $(JCLASS) ./src/*.java

test: 	src/$(MAIN).class
       	$(JVM) $(JCLASS) org.junit.runner.JUnitCore $(MAIN)

doc: 	mkdir doc
     	javadoc -d doc -sourcepath ./src

clean: 	$(RM) ./src/*.class