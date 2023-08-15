from slash.frontend.main import main
import slash

slash.config.root.log.root = '../logs'
slash.config.root.run.default_sources = ["tests"]

if __name__ == "__main__":

    main()