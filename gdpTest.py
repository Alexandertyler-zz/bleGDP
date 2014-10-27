import gdpAccess

def main():
    gdp = gdpAccess.GDP("/home/alex/Cs/Swarm/ble/gdp/")
    #gdp.startServer()
    gcl = gdp.getGCL()
    gdp.gdpPOST(20, gcl)

if __name__ == "__main__":
    main()
