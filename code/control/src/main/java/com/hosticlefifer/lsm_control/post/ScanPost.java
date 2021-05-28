package com.hosticlefifer.lsm_control.post;


import com.hosticlefifer.lsm_control.data_handling.DataPoint;
import com.hosticlefifer.lsm_control.data_handling.Scan;
import org.jzy3d.maths.Coord3d;

import java.util.ArrayList;
import java.util.LinkedHashMap;

/**
 * For scan post-processors
 */
public abstract class ScanPost {

    protected final LinkedHashMap<Coord3d, DataPoint> toLinkedHashMap(ArrayList<DataPoint> points) {
        LinkedHashMap<Coord3d, DataPoint> dataMap = new LinkedHashMap<>();
        for(DataPoint point : points)
            dataMap.put(new Coord3d(point.getX(), point.getY(), point.getZ()), point);
        return dataMap;
    }

    protected final LinkedHashMap<Coord3d, DataPoint> toLinkedHashMap(Scan scan) {
        return toLinkedHashMap(scan.getDataPoints());
    }


    public abstract void process(LinkedHashMap<Coord3d, DataPoint> points);
}
