"""トンネルモデル (./tun/)"""

from .base import (
    Attribute,
    AttributeGroup,
    FacilityAttributePaths,
    FeatureProcessingDefinition,
    GeometricAttribute,
    GeometricAttributes,
)

TUNNEL = FeatureProcessingDefinition(
    id="tun:Tunnel",
    name="Tunnel",
    target_elements=["tun:Tunnel"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./tun:class",
                    datatype="string",
                    predefined_codelist="Tunnel_class",
                ),
                Attribute(
                    name="function",
                    path="./tun:function",
                    datatype="[]string",
                    predefined_codelist="Tunnel_function",
                ),
                Attribute(
                    name="yearOfConstruction",
                    path="./tun:yearOfConstruction",
                    datatype="integer",
                ),
                Attribute(
                    name="yearOfDemolition",
                    path="./tun:yearOfDemolition",
                    datatype="integer",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tunBaseAttribute/uro:ConstructionBaseAttribute",
            attributes=[
                Attribute(
                    name="adminOffice",
                    path="./uro:adminOffice",
                    datatype="string",
                ),
                Attribute(
                    name="adminType",
                    path="./uro:adminType",
                    datatype="string",
                    predefined_codelist="ConstructionBaseAttribute_adminType",
                ),
                Attribute(
                    name="administorator",
                    path="./uro:administorator",
                    datatype="string",
                ),
                Attribute(
                    name="completionYear",
                    path="./uro:completionYear",
                    datatype="integer",
                ),
                Attribute(
                    name="constructionStartYear",
                    path="./uro:constructionStartYear",
                    datatype="integer",
                ),
                Attribute(
                    name="facilityAge",
                    path="./uro:facilityAge",
                    datatype="integer",
                ),
                Attribute(
                    name="installer",
                    path="./uro:installer",
                    datatype="string",
                ),
                Attribute(
                    name="installerType",
                    path="./uro:installerType",
                    datatype="string",
                    predefined_codelist="ConstructionBaseAttribute_installerType",
                ),
                Attribute(
                    name="kana",
                    path="./uro:kana",
                    datatype="string",
                ),
                Attribute(
                    name="operatorType",
                    path="./uro:operatorType",
                    datatype="string",
                    predefined_codelist=None,
                ),
                Attribute(
                    name="purpose",
                    path="./uro:purpose",
                    datatype="string",
                    predefined_codelist="ConstructionBaseAttribute_purpose",
                ),
                Attribute(
                    name="specification",
                    path="./uro:specification",
                    datatype="string",
                ),
                Attribute(
                    name="structureOrdinance",
                    path="./uro:structureOrdinance",
                    datatype="string",
                ),
                Attribute(
                    name="update",
                    path="./uro:update",
                    datatype="date",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tunStructureAttribute/uro:TunnelStructureAttribute",
            attributes=[
                Attribute(
                    name="area",
                    path="./uro:area",
                    datatype="double",
                ),
                Attribute(
                    name="effectiveHeight",
                    path="./uro:effectiveHeight",
                    datatype="double",
                ),
                Attribute(
                    name="innerHeight",
                    path="./uro:innerHeight",
                    datatype="double",
                ),
                Attribute(
                    name="length",
                    path="./uro:length",
                    datatype="double",
                ),
                Attribute(
                    name="mouthType",
                    path="./uro:mouthType",
                    datatype="string",
                    predefined_codelist="TunnelStructureAttribute_mouthType",
                ),
                Attribute(
                    name="slopeType",
                    path="./uro:slopeType",
                    datatype="string",
                    predefined_codelist="ConstructionStructureAttribute_slopeType",
                ),
                Attribute(
                    name="tunnelSubtype",
                    path="./uro:tunnelSubtype",
                    datatype="string",
                    predefined_codelist="TunnelStructureAttribute_tunnelSubType",
                ),
                Attribute(
                    name="tunnelType",
                    path="./uro:tunnelType",
                    datatype="string",
                    predefined_codelist="TunnelStructureAttribute_tunnelType",
                ),
                Attribute(
                    name="width",
                    path="./uro:width",
                    datatype="double",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tunFunctionalAttribute/uro:TunnelFunctionalAttribute",
            attributes=[
                Attribute(
                    name="directionType",
                    path="./uro:directionType",
                    datatype="string",
                    predefined_codelist="ConstructionFunctionalAttribute_directionType",
                ),
                Attribute(
                    name="userType",
                    path="./uro:userType",
                    datatype="string",
                    predefined_codelist="TunnelFunctionalAttribute_userType",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tunRiskAssessmentAttribute/uro:ConstructionRiskAssessmentAttribute",
            attributes=[
                Attribute(
                    name="referenceDate",
                    path="./uro:referenceDate",
                    datatype="date",
                ),
                Attribute(
                    name="riskType",
                    path="./uro:riskType",
                    datatype="[]string",
                    predefined_codelist="ConstructionRiskAssessmentAttribute_riskType",
                ),
                Attribute(
                    name="status",
                    path="./uro:status",
                    datatype="[]string",
                    predefined_codelist="ConstructionRiskAssessmentAttribute_status",
                ),
                Attribute(
                    name="surveyYear",
                    path="./uro:surveyYear",
                    datatype="integer",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tunDataQualityAttribute/uro:ConstructionDataQualityAttribute",
            attributes=[
                Attribute(
                    name="appearanceSrcDesc",
                    path="./uro:appearanceSrcDesc",
                    datatype="[]string",
                    predefined_codelist="DataQualityAttribute_appearanceSrcDesc",
                ),
                Attribute(
                    name="dataAcquisition",
                    path="./uro:dataAcquisition",
                    datatype="string",
                ),
                Attribute(
                    name="geometrySrcDesc",
                    path="./uro:geometrySrcDesc",
                    datatype="[]string",
                    predefined_codelist="DataQualityAttribute_geometrySrcDesc",
                ),
                Attribute(
                    name="lod1HeightType",
                    path="./uro:lod1HeightType",
                    datatype="string",
                    predefined_codelist="DataQualityAttribute_lod1HeightType",
                ),
                Attribute(
                    name="lodType",
                    path="./uro:lodType",
                    datatype="[]string",
                    predefined_codelist="Tunnel_lodType",
                ),
                Attribute(
                    name="photoScale",
                    path="./uro:photoScale",
                    datatype="integer",
                ),
                Attribute(
                    name="srcScale",
                    path="./uro:srcScale",
                    datatype="string",
                    predefined_codelist="DataQualityAttribute_srcScale",
                ),
                Attribute(
                    name="thematicSrcDesc",
                    path="./uro:thematicSrcDesc",
                    datatype="[]string",
                    predefined_codelist="DataQualityAttribute_thematicSrcDesc",
                ),
            ],
        ),
    ],
    disaster_risk_attr_conatiner_path="./uro:tunDisasterRiskAttribute",
    dm_attr_container_path="./uro:tunDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:tunFacilityIdAttribute",
        facility_types="./uro:tunFacilityTypeAttribute",
        facility_attrs="./uro:tunFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod1=GeometricAttribute(
            lod_detection=["./tun:lod1Solid"],
            collect_all=[".//tun:lod1Solid//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            lod_detection=["./tun:lod2Solid"],
            collect_all=[
                ".//tun:lod2MultiSurface//gml:Polygon",
                ".//tun:lod2Geometry//gml:Polygon",
            ],
            only_direct=["./tun:lod2Solid//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tun:lod3Solid"],
            collect_all=[
                ".//tun:lod3MultiSurface//gml:Polygon",
                ".//tun:lod3Geometry//gml:Polygon",
                ".//tun:lod3Solid//gml:Polygon",
            ],
            only_direct=["./tun:lod3Solid//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./tun:lod4Solid", "./tun:lod4MultiSurface"],
            collect_all=[
                ".//tun:lod4MultiSurface//gml:Polygon",
                ".//tun:lod4Geometry//gml:Polygon",
                ".//tun:lod4Solid//gml:Polygon",
            ],
            only_direct=[
                "./tun:lod4MultiSurface//gml:Polygon",
                "./tun:lod4Solid//gml:Polygon",
            ],
        ),
        semantic_parts=[
            ".//tun:GroundSurface",
            ".//tun:WallSurface",
            ".//tun:RoofSurface",
            ".//tun:OuterCeilingSurface",
            ".//tun:OuterFloorSurface",
            ".//tun:ClosureSurface",
            ".//tun:CeilingSurface",
            ".//tun:InteriorWallSurface",
            ".//tun:FloorSurface",
            ".//tun:TunnelInstallation",
            ".//tun:IntTunnelInstallation",
            ".//tun:TunnelFurniture",
            # TODO: 現状、tun:HollowSpace と tun:TunnelPart の概念は考慮していない
        ],
    ),
)

TUNNEL_BOUNDARY_SURFACE = FeatureProcessingDefinition(
    id="tun:_BoundarySurface",
    name="BoundarySurface",
    target_elements=[
        "tun:GroundSurface",
        "tun:WallSurface",
        "tun:RoofSurface",
        "tun:OuterCeilingSurface",
        "tun:OuterFloorSurface",
        "tun:ClosureSurface",
        "tun:CeilingSurface",
        "tun:InteriorWallSurface",
        "tun:FloorSurface",
    ],
    attribute_groups=[],
    geometries=GeometricAttributes(
        lod2=GeometricAttribute(
            lod_detection=["./tun:lod2MultiSurface"],
            collect_all=[".//tun:lod2MultiSurface//gml:Polygon"],
            only_direct=["./tun:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tun:lod3MultiSurface"],
            collect_all=[".//tun:lod3MultiSurface//gml:Polygon"],
            only_direct=["./tun:lod3MultiSurface//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./tun:lod4MultiSurface"],
            collect_all=[".//tun:lod4MultiSurface//gml:Polygon"],
            only_direct=["./tun:lod4MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./tun:opening/tun:Door",
            "./tun:opening/tun:Window",
        ],
    ),
)

TUNNEL_OPENING = FeatureProcessingDefinition(
    id="tun:_Opening",
    name="Opening",
    target_elements=[
        "tun:Window",
        "tun:Door",
    ],
    attribute_groups=[],
    geometries=GeometricAttributes(
        lod3=GeometricAttribute(
            lod_detection=["./tun:lod3MultiSurface"],
            collect_all=[".//tun:lod3MultiSurface//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./tun:lod4MultiSurface"],
            collect_all=[".//tun:lod4MultiSurface//gml:Polygon"],
        ),
    ),
)

TUNNEL_INSTALLATION = FeatureProcessingDefinition(
    id="tun:TunnelInstallation",
    name="TunnelInstallation",
    target_elements=[
        "tun:TunnelInstallation",
    ],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="function",
                    path="./tun:function",
                    datatype="[]string",
                    predefined_codelist="TunnelInstallation_function",
                ),
            ],
        )
    ],
    geometries=GeometricAttributes(
        lod2=GeometricAttribute(
            lod_detection=["./tun:lod2Geometry"],
            collect_all=[".//tun:lod2Geometry//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tun:lod3Geometry"],
            collect_all=[".//tun:lod3Geometry//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./tun:lod4Geometry"],
            collect_all=[".//tun:lod4Geometry//gml:Polygon"],
        ),
    ),
)

TUNNEL_INT_INSTALLATION = FeatureProcessingDefinition(
    id="tun:IntTunnelInstallation",
    name="IntTunnelInstallation",
    target_elements=[
        "tun:IntTunnelInstallation",
    ],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="function",
                    path="./tun:function",
                    datatype="[]string",
                    predefined_codelist="TunnelInstallation_function",
                ),
            ],
        ),
    ],
    geometries=GeometricAttributes(
        lod3=GeometricAttribute(
            lod_detection=["./tun:lod3Geometry"],
            collect_all=[".//tun:lod3Geometry//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./tun:lod4Geometry"],
            collect_all=[".//tun:lod4Geometry//gml:Polygon"],
        ),
    ),
)


TUNNEL_FURNITURE = FeatureProcessingDefinition(
    id="tun:TunnelFurniture",
    name="TunnelFurniture",
    target_elements=[
        "tun:TunnelFurniture",
    ],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="function",
                    path="./tun:function",
                    datatype="[]string",
                    predefined_codelist="TunnelInstallation_function",
                ),
            ],
        ),
    ],
    geometries=GeometricAttributes(
        lod4=GeometricAttribute(
            lod_detection=["./tun:lod4Geometry"],
            collect_all=[".//tun:lod4Geometry//gml:Polygon"],
        ),
    ),
)