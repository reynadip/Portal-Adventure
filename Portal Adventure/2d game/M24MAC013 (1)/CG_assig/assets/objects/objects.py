import numpy as np
import math

def CreateCircle(center, radius, colour, points = 10, offset = 0, semi = False):
    vertices = [center[0], center[1], center[2], colour[0], colour[1], colour[2]]
    indices = []

    if semi == True:
        for i in range(points+1):
            vertices += [
                center[0] + radius * np.cos(float(i * np.pi)/points),
                center[1] + radius * np.sin(float(i * np.pi)/points),
                center[2],
                colour[0],
                colour[1],
                colour[2],
                ]
            
            ind1 = i+1
            ind2 = i+2 if i != points else 1
            indices += [0 + offset, ind1 + offset, ind2 + offset]
    else:
        for i in range(points):
            vertices += [
                center[0] + radius * np.cos(float(i * 2* np.pi)/points),
                center[1] + radius * np.sin(float(i * 2* np.pi)/points),
                center[2],
                colour[0],
                colour[1],
                colour[2],
                ]
            
            ind1 = i+1
            ind2 = i+2 if i != points-1 else 1
            indices += [0 + offset, ind1 + offset, ind2 + offset]

    return (vertices, indices)    

obj1Verts, obj1Inds = CreateCircle([0,0,0],1, [0.769,0.769,0.769], 20)
obj1Props = {
    'vertices' : np.array(obj1Verts, dtype = np.float32),
    
    'indices' : np.array(obj1Inds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32),
    'accleration':np.array([0, 0, 0], dtype = np.float32)
}


def CreateCircle(center, radius, color, segments, index_offset):
    x, y, z = center
    vertices = []
    indices = []
    angle_step = 2 * np.pi / segments

    for i in range(segments):
        theta = i * angle_step
        next_theta = (i + 1) * angle_step

        # Current point
        x1 = x + radius * np.cos(theta)
        y1 = y + radius * np.sin(theta)

        # Next point
        x2 = x + radius * np.cos(next_theta)
        y2 = y + radius * np.sin(next_theta)

        # Add center, current, and next vertices
        vertices += [
            x, y, z, *color,  # Center
            x1, y1, z, *color,  # Current point
            x2, y2, z, *color   # Next point
        ]

        indices += [
            index_offset, index_offset + 1, index_offset + 2
        ]
        index_offset += 3

    return vertices, indices

def CreateRectangle(center, width, height, color, index_offset):
    x, y, z = center
    vertices = [
        x - width / 2, y - height / 2, z, *color,  # Bottom left
        x + width / 2, y - height / 2, z, *color,  # Bottom right
        x - width / 2, y + height / 2, z, *color,  # Top left
        x + width / 2, y + height / 2, z, *color   # Top right
    ]
    indices = [
        index_offset, index_offset + 1, index_offset + 2,
        index_offset + 2, index_offset + 1, index_offset + 3
    ]
    return vertices, indices

def CreateTriangle(center, size, color, index_offset):
    x, y, z = center
    vertices = [
        x, y + size, z, *color,  # Top vertex
        x - size / 2, y - size / 2, z, *color,  # Bottom left vertex
        x + size / 2, y - size / 2, z, *color   # Bottom right vertex
    ]
    indices = [
        index_offset, index_offset + 1, index_offset + 2
    ]
    return vertices, indices



def CreateHexagon(center, radius, color, segments, index_offset=0):
    vertices = []
    indices = []

    # Add center vertex (for triangle fan)
    vertices.extend([center[0], center[1], center[2], color[0], color[1], color[2]])
    
    # Compute hexagon vertices
    for i in range(segments):
        angle = (2 * math.pi * i) / segments  # Divide full circle into 6 parts
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        z = center[2]  # Same depth as center
        vertices.extend([x, y, z, color[0], color[1], color[2]])

    # Create indices for triangle fan
    for i in range(1, segments):
        indices.extend([index_offset, index_offset + i, index_offset + i + 1])
    
    # Last triangle (closing the fan)
    indices.extend([index_offset, index_offset + segments, index_offset + 1])

    return vertices, indices

import numpy as np
import math

def CreateOval(center, radius_x, radius_y, color, segments, index_offset=0):
    vertices = []
    indices = []

    # Add center vertex (for triangle fan)
    vertices.extend([center[0], center[1], center[2], color[0], color[1], color[2]])

    # Compute oval boundary points
    for i in range(segments):
        angle = (2 * math.pi * i) / segments  # Divide full circle into segments
        x = center[0] + radius_x * math.cos(angle)  # X-radius is different
        y = center[1] + radius_y * math.sin(angle)  # Y-radius is different
        z = center[2]  # Same depth as center
        vertices.extend([x, y, z, color[0], color[1], color[2]])

    # Create indices for triangle fan
    for i in range(1, segments):
        indices.extend([index_offset, index_offset + i, index_offset + i + 1])

    # Last triangle (closing the fan)
    indices.extend([index_offset, index_offset + segments, index_offset + 1])

    return vertices, indices

import numpy as np

def CreateDiamond(center, width, height, color, index_offset=0):
    vertices = []
    indices = []

    # Define the four points of the diamond (relative to center)
    top =    [center[0], center[1] + height / 2, center[2]]
    bottom = [center[0], center[1] - height / 2, center[2]]
    left =   [center[0] - width / 2, center[1], center[2]]
    right =  [center[0] + width / 2, center[1], center[2]]

    # Create vertex data (position + color)
    for point in [top, bottom, left, right]:
        vertices.extend(point + color)  # (x, y, z, r, g, b)

    # Define two triangles using indices
    indices.extend([
        index_offset, index_offset + 2, index_offset + 1,  # Top - Left - Bottom
        index_offset, index_offset + 1, index_offset + 3   # Top - Bottom - Right
    ])

    return vertices, indices


def CreateAngryBird():
    vertices = []
    indices = []

    # Main body (hexagon)
    body_verts, body_inds = CreateHexagon([0.0, 0.0, 0.0], 1.0, [1.0, 0.0, 0.0], 6, 0)
    vertices += body_verts
    indices += body_inds
    index_offset = len(vertices) // 6

    # Left Eye (Oval)
    left_eye_verts, left_eye_inds = CreateOval([-0.35, 0.3, 0.1], 0.25, 0.15, [1.0, 1.0, 1.0], 20, index_offset)
    vertices += left_eye_verts
    indices += left_eye_inds
    index_offset += 20 + 1

    # Right Eye (Oval)
    right_eye_verts, right_eye_inds = CreateOval([0.35, 0.3, 0.1], 0.25, 0.15, [1.0, 1.0, 1.0], 20, index_offset)
    vertices += right_eye_verts
    indices += right_eye_inds
    index_offset += 20 + 1

    # Left Pupil
    left_pupil_verts, left_pupil_inds = CreateCircle([-0.3, 0.3, 0.15], 0.1, [0.0, 0.0, 0.0], 10, index_offset)
    vertices += left_pupil_verts
    indices += left_pupil_inds
    index_offset += 10 + 1

    # Right Pupil
    right_pupil_verts, right_pupil_inds = CreateCircle([0.3, 0.3, 0.15], 0.1, [0.0, 0.0, 0.0], 10, index_offset)
    vertices += right_pupil_verts
    indices += right_pupil_inds
    index_offset += 10 + 1

    # Beak (Diamond Shape)
    beak_verts, beak_inds = CreateDiamond([0.0, -0.2, 0.1], 0.3, 0.2, [1.0, 0.6, 0.0], index_offset)
    vertices += beak_verts
    indices += beak_inds
    index_offset += 4

    # Left Eyebrow (Thicker & Angled)
    left_brow_verts, left_brow_inds = CreateRectangle([-0.4, 0.6, 0.1], 0.5, 0.1, [1.0, 0.0, 0.0], index_offset)
    vertices += left_brow_verts
    indices += left_brow_inds
    index_offset += 4

    # Right Eyebrow (Thicker & Angled)
    right_brow_verts, right_brow_inds = CreateRectangle([0.4, 0.6, 0.1], 0.5, 0.1, [1.0, 0.0, 0.0], index_offset)
    vertices += right_brow_verts
    indices += right_brow_inds
    index_offset += 4

    # Belly (Smaller white circle)
    belly_verts, belly_inds = CreateCircle([0.0, -0.6, 0.1], 0.4, [1.0, 1.0, 1.0], 20, index_offset)
    vertices += belly_verts
    indices += belly_inds
    index_offset += 20 + 1

    # Feathers on top (Three small triangles)
    feather1_verts, feather1_inds = CreateTriangle([0.0, 1.1, 0.1], 0.2, [1.0, 0.0, 0.0], index_offset)
    vertices += feather1_verts
    indices += feather1_inds
    index_offset += 3

    feather2_verts, feather2_inds = CreateTriangle([-0.15, 1.0, 0.1], 0.2, [1.0, 0.0, 0.0], index_offset)
    vertices += feather2_verts
    indices += feather2_inds
    index_offset += 3

    feather3_verts, feather3_inds = CreateTriangle([0.15, 1.0, 0.1], 0.2, [1.0, 0.0, 0.0], index_offset)
    vertices += feather3_verts
    indices += feather3_inds

    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)


def CreatePlayer():

    vertices, indices = CreateCircle([0.0, 0.0, 0.0], 1.0, [220/255, 183/255, 139/255], 50, 0)

    eye_verts1, eye_inds1 = CreateCircle([0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
    vertices += eye_verts1
    indices += eye_inds1

    eye_verts2, eye_inds2 = CreateCircle([-0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
    vertices += eye_verts2
    indices += eye_inds2

    eye_verts3, eye_inds3 = CreateCircle([-0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
    vertices += eye_verts3
    indices += eye_inds3

    eye_verts4, eye_inds4 = CreateCircle([0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
    vertices += eye_verts4
    indices += eye_inds4

    eye_verts5, eye_inds5 = CreateCircle([0.0, 0.0, 0.2], 1.0, [1,0,0], 25, len(vertices)/6, True)
    vertices += eye_verts5
    indices += eye_inds5

    eye_verts6, eye_inds6 = CreateCircle([0.0, 0.95, 0.3], 0.3, [0.9,0.9,0.9], 20, len(vertices)/6)
    vertices += eye_verts6
    indices += eye_inds6

    return vertices, indices

def CreateBackground(grassColour, waterColour, position_offsets):
    # Vertices defining the background layout
    vertices = [
        -500.0 + position_offsets[0], 500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],
        -400.0 + position_offsets[0], 500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],
        -400.0 + position_offsets[0], -500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],
        -500.0 + position_offsets[0], -500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],

        500.0 + position_offsets[0], 500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],
        400.0 + position_offsets[0], 500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],
        400.0 + position_offsets[0], -500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],
        500.0 + position_offsets[0], -500.0 + position_offsets[1], -0.9, grassColour[0], grassColour[1], grassColour[2],

        -400.0 + position_offsets[0], 500.0 + position_offsets[1], -0.9, waterColour[0], waterColour[1], waterColour[2],
        400.0 + position_offsets[0], 500.0 + position_offsets[1], -0.9, waterColour[0], waterColour[1], waterColour[2],
        400.0 + position_offsets[0], -500.0 + position_offsets[1], -0.9, waterColour[0], waterColour[1], waterColour[2],
        -400.0 + position_offsets[0], -500.0 + position_offsets[1], -0.9, waterColour[0], waterColour[1], waterColour[2],
    ]

    indices = [
        0, 1, 2, 0, 3, 2,
        8, 9, 10, 8, 11, 10,
        4, 5, 6, 4, 7, 6
    ]

    return vertices, indices


# Background 1: Fresh Green Grass and Blue Water (Default)
grassColour1 = [0, 1, 0]  # Bright green grass
waterColour1 = [0, 0, 1]  # Blue water
backgroundVerts, backgroundInds = CreateBackground(grassColour1, waterColour1, [0, 0])
backgroundProps = {
    'vertices': np.array(backgroundVerts, dtype=np.float32),
    'indices': np.array(backgroundInds, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'boundary': [500.0, -500.0, 500.0, 500.0],
    'river_banks': [-400.0, 400.0]
}

# Background 2: Desert Vibe with Yellow Sand and Red-Tinted Water
grassColour2 = [1, 1, 0]  # Yellow sand
waterColour2 = [1, 0, 0]  # Red-tinted water
backgroundVerts2, backgroundInds2 = CreateBackground(grassColour2, waterColour2, [0, -100])
backgroundProps2 = {
    'vertices': np.array(backgroundVerts2, dtype=np.float32),
    'indices': np.array(backgroundInds2, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'boundary': [500.0, -500.0, 500.0, 500.0],
    'river_banks': [-400.0, 400.0]
}

# Background 3: Sunset with Orange Grass and Purple Water
grassColour3 = [1, 0.5, 0]  # Sunset orange grass
waterColour3 = [0.5, 0, 0.5]  # Purple water
backgroundVerts3, backgroundInds3 = CreateBackground(grassColour3, waterColour3, [0, -200])
backgroundProps3 = {
    'vertices': np.array(backgroundVerts3, dtype=np.float32),
    'indices': np.array(backgroundInds3, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'boundary': [500.0, -500.0, 500.0, 500.0],
    'river_banks': [-400.0, 400.0]
}

playerVerts, playerInds = CreateAngryBird()
playerProps = {
    'vertices' : np.array(playerVerts, dtype = np.float32),
    
    'indices' : np.array(playerInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32),
    'acceleration':np.array([0, 0, 0], dtype = np.float32)
}

# backgroundVerts, backgroundInds = CreateBackground()
# backgroundProps = {
#     'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
#     'indices' : np.array(backgroundInds, dtype = np.uint32),

#     'position' : np.array([0, 0, 0], dtype = np.float32),

#     'rotation_z' : 0.0,

#     'scale' : np.array([1, 1, 1], dtype = np.float32),

#     'boundary' : [500.0, -500.0, 500.0, 500.0],

#     'river_banks': [-400.0, 400.0]
# }



def CreateGreenFrog(center, radius, segments, index_offset=0):
    vertices = []
    indices = []

    # Face (big green circle)
    face_verts, face_inds = CreateCircle(center, radius, [0.0, 1.0, 0.0], segments, index_offset)
    vertices += face_verts
    indices += face_inds
    index_offset += segments + 1

    # Left Eye (raised, bigger white circle)
    left_eye_verts, left_eye_inds = CreateCircle(
        [center[0] - radius * 0.35, center[1] + radius * 0.55, center[2] + 0.1],
        radius * 0.35, [1.0, 1.0, 1.0], segments, index_offset
    )
    vertices += left_eye_verts
    indices += left_eye_inds
    index_offset += segments + 1

    # Right Eye (raised, bigger white circle)
    right_eye_verts, right_eye_inds = CreateCircle(
        [center[0] + radius * 0.35, center[1] + radius * 0.55, center[2] + 0.1],
        radius * 0.35, [1.0, 1.0, 1.0], segments, index_offset
    )
    vertices += right_eye_verts
    indices += right_eye_inds
    index_offset += segments + 1

    # Left Pupil (black, further enlarged)
    left_pupil_verts, left_pupil_inds = CreateCircle(
        [center[0] - radius * 0.25, center[1] + radius * 0.55, center[2] + 0.2],
        radius * 0.2, [0.0, 0.0, 0.0], segments, index_offset  # Increased size of the pupil
    )
    vertices += left_pupil_verts
    indices += left_pupil_inds
    index_offset += segments + 1

    # Right Pupil (black, further enlarged)
    right_pupil_verts, right_pupil_inds = CreateCircle(
        [center[0] + radius * 0.25, center[1] + radius * 0.55, center[2] + 0.2],
        radius * 0.2, [0.0, 0.0, 0.0], segments, index_offset  # Increased size of the pupil
    )
    vertices += right_pupil_verts
    indices += right_pupil_inds
    index_offset += segments + 1

    # Nose (bigger nostrils and repositioned)
    left_nostril_verts, left_nostril_inds = CreateCircle(
        [center[0] - radius * 0.2, center[1] - radius * 0.05, center[2] + 0.2],  # Repositioned
        radius * 0.2, [0.0, 0.0, 0.0], segments, index_offset  # Increased size of nostril
    )
    vertices += left_nostril_verts
    indices += left_nostril_inds
    index_offset += segments + 1

    right_nostril_verts, right_nostril_inds = CreateCircle(
        [center[0] + radius * 0.2, center[1] - radius * 0.05, center[2] + 0.2],  # Repositioned
        radius * 0.2, [0.0, 0.0, 0.0], segments, index_offset  # Increased size of nostril
    )
    vertices += right_nostril_verts
    indices += right_nostril_inds
    index_offset += segments + 1

    return vertices, indices


# Example enemy properties
enemyVerts, enemyInds = CreateGreenFrog([0, 0, 0], 30, 20)
enemyProps = {
    'vertices': np.array(enemyVerts, dtype=np.float32),
    'indices': np.array(enemyInds, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'velocity': np.array([0, 0, 0], dtype=np.float32)
}


#CreateRectangle(center, width, height, color, index_offset):
entryVerts,entryinds= CreateCircle([0,0,0], 50, [0.6,0.1,0], 20, 0)
entryProps={
    'vertices':np.array(entryVerts,dtype=np.float32),
    'indices':np.array(entryinds, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'velocity': np.array([0, 0, 0], dtype=np.float32)
}

exitverts, exitinds= CreateCircle([0,0,0], 50, [0.6,0.1,0], 20, 0)
exitProps={
    'vertices':np.array(exitverts,dtype=np.float32),
    'indices':np.array(exitinds, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'velocity': np.array([0, 0, 0], dtype=np.float32)
}   





# def CreateBackground2():
#     # Colors
#     sandColour = [237/255, 201/255, 175/255]   # Light brown sand color
#     duneColour = [194/255, 178/255, 128/255]   # Slightly darker dunes
#     skyColour = [255/255, 153/255, 51/255]     # Warm sunset sky

#     # Background (Sky and Sand)
#     vertices = [
#         # Sky
#         -500.0, 500.0, -0.9, skyColour[0], skyColour[1], skyColour[2],
#         500.0, 500.0, -0.9, skyColour[0], skyColour[1], skyColour[2],
#         500.0, 100.0, -0.9, skyColour[0], skyColour[1], skyColour[2],
#         -500.0, 100.0, -0.9, skyColour[0], skyColour[1], skyColour[2],

#         # Sand (Base ground)
#         -500, 100.0, -0.9,   sandColour[0], sandColour[1], sandColour[2],
#         500, 100.0, -0.9,    sandColour[0], sandColour[1], sandColour[2],
#         500, -500, -0.9,      sandColour[0], sandColour[1], sandColour[2],
#         -500, -500, -0.9,     sandColour[0], sandColour[1], sandColour[2],

#         # Dune (Midground for extra detail)
#         -300, 50, -0.9,   duneColour[0], duneColour[1], duneColour[2],
#         300, 50, -0.9,    duneColour[0], duneColour[1], duneColour[2],
#         400, -100, -0.9,  duneColour[0], duneColour[1], duneColour[2],
#         -400, -100, -0.9, duneColour[0], duneColour[1], duneColour[2],
#     ]

#     indices = [
#         0, 1, 2,  0, 3, 2,   # Sky
#         4, 5, 6,  4, 7, 6,   # Sand
#         8, 9, 10, 8, 11, 10  # Dunes
#     ]

#     return vertices, indices


# backgroundVerts2, backgroundInds2 = CreateBackground2()
# backgroundProps2 = {
#     'vertices' : np.array(backgroundVerts2, dtype = np.float32),
    
#     'indices' : np.array(backgroundInds2, dtype = np.uint32),

#     'position' : np.array([0, 0, 0], dtype = np.float32),

#     'rotation_z' : 0.0,

#     'scale' : np.array([1, 1, 1], dtype = np.float32),

#     'boundary' : [500.0, -500.0, 500.0, 500.0],

#     'dune_banks': [-300.0, 300.0]
# }


# def CreateBackground3():
#     # Define colors for the new background
#     sunsetSky = [255/255, 102/255, 0/255]  # Sunset orange
#     darkSky = [128/255, 0/255, 64/255]  # Dark purple (top sky)
#     groundColour = [105/255, 105/255, 105/255]  # Dark gray (rocky terrain)
    
#     vertices = [
#         # Sky (Top Half - Gradient Effect)
#         -500.0, 500.0, -0.9, darkSky[0], darkSky[1], darkSky[2],  # Top-left
#         500.0, 500.0, -0.9, darkSky[0], darkSky[1], darkSky[2],   # Top-right
#         500.0, 100.0, -0.9, sunsetSky[0], sunsetSky[1], sunsetSky[2],   # Middle-right
#         -500.0, 100.0, -0.9, sunsetSky[0], sunsetSky[1], sunsetSky[2],  # Middle-left

#         # Ground (Rocky Terrain)
#         -500, 100.0, -0.9, groundColour[0], groundColour[1], groundColour[2],  # Middle-left
#         500, 100.0, -0.9, groundColour[0], groundColour[1], groundColour[2],   # Middle-right
#         500, -500, -0.9, groundColour[0], groundColour[1], groundColour[2],    # Bottom-right
#         -500, -500, -0.9, groundColour[0], groundColour[1], groundColour[2],   # Bottom-left
#     ]

#     indices = [
#         0, 1, 2,  # Sky upper triangle
#         0, 2, 3,  # Sky lower triangle
#         4, 5, 6,  # Ground upper triangle
#         4, 6, 7   # Ground lower triangle
#     ]

#     return vertices, indices

# backgroundVerts3, backgroundInds3 = CreateBackground3()
# backgroundProps3 = {
#     'vertices' : np.array(backgroundVerts3, dtype = np.float32),
    
#     'indices' : np.array(backgroundInds3, dtype = np.uint32),

#     'position' : np.array([0, 0, 0], dtype = np.float32),

#     'rotation_z' : 0.0,

#     'scale' : np.array([1, 1, 1], dtype = np.float32),

#     'boundary': [500.0, -500.0, 500.0, -500.0]
# }










import numpy as np

def CreateKey(center=[0, 0, 0], shaft_width=1, shaft_height=4, 
              head_radius=2, notch_size=0.6, color=[1.0, 1.0, 0.0], segments=20):

    vertices = []
    indices = []
    index_offset = 0

    # **1. Create the shaft (rectangle)**
    shaft_verts, shaft_inds = CreateRectangle(
        [center[0], center[1] - shaft_height / 2, center[2]], shaft_width, shaft_height, color, index_offset
    )
    vertices += shaft_verts
    indices += shaft_inds
    index_offset += 4  # Since a rectangle has 4 vertices

    # **2. Create the key head (circle)**
    head_verts, head_inds = CreateCircle(
        [center[0], center[1] + shaft_height / 2 + head_radius, center[2]], head_radius, color, segments, index_offset
    )
    vertices += head_verts
    indices += head_inds
    index_offset += segments + 1

    # **3. Create Notches (small rectangles)**
    notch_1_verts, notch_1_inds = CreateRectangle(
        [center[0] - shaft_width / 3, center[1] - shaft_height / 2 - notch_size / 2, center[2]], 
        notch_size, notch_size, color, index_offset
    )
    vertices += notch_1_verts
    indices += notch_1_inds
    index_offset += 4

    notch_2_verts, notch_2_inds = CreateRectangle(
        [center[0] + shaft_width / 3, center[1] - shaft_height / 2 - notch_size / 2, center[2]], 
        notch_size, notch_size, color, index_offset
    )
    vertices += notch_2_verts
    indices += notch_2_inds

    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)

# Define Key Object Properties
keyVerts, keyInds = CreateKey()
keyProps = {
    'vertices': np.array(keyVerts, dtype=np.float32),
    'indices': np.array(keyInds, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
}
