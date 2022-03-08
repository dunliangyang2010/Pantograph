import xml.etree.ElementTree as ET
import os
import glob

class_dict ={ 'pantograph':0, 'flash':1, }

src_dir = input('enter src_dir:')
des_dir = input('enter des_dir:')

for xml in glob.glob(os.path.join(src_dir, '*.xml')):
    txt_path = os.path.join(des_dir, xml.split('/')[-1].split('.')[0])+ '.txt'

    # Parse .xml file
    with open(xml) as f:
        tree = ET.parse(f)
        root = tree.getroot()

        W = float(root.find('size').find('width').text)
        H = float(root.find('size').find('height').text)
        objs = root.iter('object')

        txt = open(txt_path, 'w')
        for obj in objs:
            # class
            c = obj.find('name').text
            c_name = str(class_dict.get(c))

            xmin = float(obj.find('bndbox').find('xmin').text)
            ymin = float(obj.find('bndbox').find('ymin').text)
            xmax = float(obj.find('bndbox').find('xmax').text)
            ymax = float(obj.find('bndbox').find('ymax').text)

            # x,y,w,h
            x = ((xmin + (xmax-xmin)/2) * 1.0) / W 
            y = ((ymin + (ymax-ymin)/2) * 1.0) / H 
            w = ((xmax-xmin) * 1.0) / W
            h = ((ymax-ymin) * 1.0) / H

            x = '{:.6f}'.format(x)
            y = '{:.6f}'.format(y)
            w = '{:.6f}'.format(w)
            h = '{:.6f}'.format(h)

            txt.write(c_name + ' ' + str(x) + ' ' + str(y)+ ' ' + str(w) + ' ' + str(h))
            txt.write('\n')
        txt.close()
