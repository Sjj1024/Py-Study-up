    for i in file_list:
        logger.info(f"开始替换{i}")
        with open(i, "r+", encoding="utf-8") as f:
            content = f.read()
            first = content.replace("<LteConfig>", '<CarrConfig carrier="PCC" name="L1" rat="LTE">')
            second = first.replace("</LteConfig>", '</CarrConfig>')
            thread = second.replace("<NrConfig>", '<CarrConfig carrier="PCC" name="N1" rat="NR">')
            fourth = thread.replace("</NrConfig>", "</CarrConfig>")
            f.seek(0)
            f.truncate()
            f.write(fourth)
        logger.info(f"替换完成{i}--->")
